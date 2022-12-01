<template>
    <update v-bind:update="false" form-title="Registrar"></update>

    <h1>Listado de categorias en componente</h1>

    <input type="text" v-model="buscar" class="form-control" placeholder="Ingrese el nombre de la categoria que desea buscar..."/>
    
    <div class="row mt-3">
    
        <div class="col-md-4" v-for="item in items" v-bind:key="item.id"> 

            <div class="card mb-3">
                <!--<img class="card-img-top" v-bind:src="'img/' + item.img" v-bind:alt="item.nombre">-->
                <div class="card-body">
                <h3 class="card-title mb-3"><strong>Nombre:</strong>{{ item.nombre }}</h3>
                <p class="card-text"><strong>Descripcion:</strong> {{ item.descripcion }}</p>
                <div><button @click="removeCategoria(item.id)">eliminar {{item.id}}</button></div>
                <button v-on:click="update =true" @click="getCategoria(item.id)">Actualizar Categoria {{item.id}}</button>
                </div>
            </div>
        </div>
    </div>
        <!--<div v-for="c in categorias" k:ey="c.id">
            <div >Nombre: {{c.nombre}} </div>
            <div >Descripcion: {{c.descripcion}} </div>
            <div><button @click="removeCategoria(c.id)">eliminar {{c.id}}</button></div>
            
            <button v-on:click="update =true" @click="cargarCategoria(c.id)">Actualizar Categoria</button>
             
        </div>-->
        <button v-on:click="update =false">Crear Categoria</button>
        <div v-if="update==true">
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h1>ACTUALIZAR CATEGORIA</h1>
                        <form @submit="sendForm2">
                            <label>Nombre: </label>
                            <input v-model="categoria.nombre" type="text" >
                            <label>Descripcion: </label>
                            <input v-model="categoria.descripcion" type="text" />
                            <!--<select  v-model="id">
                                <option v-for="c  in categorias" ::key="c.id" :value="c.id">
                                    {{c.nombre}}
                                </option>
                            </select>-->
                            <input type="submit" value="Enviar" @click="getCategoriasRefresh()">
                            <button v-on:click="update =null">cancelar</button>
                        </form>
                        
                    </div>
                </div>
            </div>
        </div>
 
        <div v-if="update==false">
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h1>REGISTRAR CATEGORIA</h1>
                        <form @submit="sendForm">
                            <label>Nombre:</label>
                            <input v-model="categoria.nombre" type="text" />
                            <label>Descripcion:</label>
                            <input v-model="categoria.descripcion" type="text" />
                            <!--<select  v-model="id">
                                <option v-for="c  in categorias" ::key="c.id" :value="c.id">
                                    {{c.nombre}}
                                </option>
                            </select>-->
                            <input type="submit" value="Enviar" @click="">
                            <button v-on:click="update =null">cancelar</button> 
                        </form>
                    </div>
            </div>
        </div>
    </div>
</template>
 
 <script>
 import axios from "axios";
 export default {
    props: {
        update: Boolean,
        formTitle: String,
        categoriaActualizar: [],
        categoria: {
                nombre:"",
                descripcion:"",
                textoABuscar: '',
            },         
    },
     data(){
         return {
            update: Boolean,
            categorias: [],
            categoria: {
                nombre:"",
                descripcion:"",
                textoABuscar: '',
            }, 
            categoriaActualizar: [],    
            buscar: '',       
         };
     },
     methods: {
        sendForm(e){
            e.preventDefault();
            
            console.log(this.categoria);
            const formData = new FormData();
            
            formData.append("nombre", this.categoria.nombre);
            formData.append("descripcion", this.categoria.descripcion);

            //this.insert(formData);
            this.addCategoria();
        },
        sendForm2(e){
            e.preventDefault();
            
            console.log(this.categoria);
            const formData = new FormData();

            formData.append("id", this.categoria.id);
            formData.append("nombre", this.categoria.nombre);
            formData.append("descripcion", this.categoria.descripcion);

            //this.insert(formData);
            this.guardar(this.categoria.id);
        },
        insert(formData)
        {
            fetch("http://localhost:3000/categoria/",{
                method: "POST",
                body: formData,
            })
                .then((res) =>res.json())
                .then((res)=>console.log(res));
        },
        async addCategoria() {
            const res = await axios.post(`http://localhost:3000/categoria`, {
                nombre: this.categoria.nombre,
                descripcion: this.categoria.descripcion,
            });
            this.categorias = [...this.categorias, res.data];
            this.nombre = "";
            this.descripcion = "";
        },

       async guardar(id){

        axios.patch(`http://localhost:3000/categoria/${id}`,
            { "nombre": this.categoria.nombre, "descripcion": this.categoria.descripcion }
           // { headers: { 'Content-Type': 'application/json', 'X-CSRF-TOKEN': crsfToken }, }
        ).then((response) => {
            // Code
            console.log("actualizado");
            this.categorias = [...this.categorias, res.data];
            this.nombre = "";
            this.descripcion = "";
            getCategoriasRefresh();
        }).catch((error) => {
            // Code
            //console.log(error);
        })
       
        },
        removeCategoria(id) {
            axios.delete(`http://localhost:3000/categoria/${id}`)
            this.categorias = this.categorias.filter(categoria => categoria.id !== id)
            console.log(categoria);
        },
        async cargarCategoria(id){
            axios.get(`http://localhost:3000/categoria/${id}`)
            this.categorias = this.categorias.filter(categoria => categoria.id !== id)
            return categoria;
            console.log(categoria.nombre + categoria.descripcion);
        },
        getCateorias(id) { //no da
            axios({
                method: "get",
                url:  `http://localhost:3000/categoria/${id}`
                //process.env.VUE_APP_RUTA_API+"/tareas/?q="+this.textoABuscar
            })
                .then(response => {
                    this.categorias = response.data;
                    console.log(response);
                })
                .catch(e => console.log(e));
        },
        getCategoriasRefresh() {
            axios({
                method: "get",
                url:  `http://localhost:3000/categoria`
                //url: process.env.VUE_APP_RUTA_API+"/tareas/?q="+this.textoABuscar
            })
                .then(response => {
                    this.categorias = response.data;
                    console.log(response);
                })
                .catch(e => console.log(e));
        },
        getCategoria(id){
            axios({
                method: "get",
                //url: process.env.VUE_APP_RUTA_API+"/tareas/"+this.$route.params.id
                url:  `http://localhost:3000/categoria/${id}`
            })
            .then(response => {
                this.categoria = response.data;
            console.log(response);
            })
            .catch(e => console.log(e));
        },
     },
     computed: {

        items() {
      return this.categorias.filter(item => {
        return item.nombre.toLowerCase().includes(this.buscar.toLowerCase());
      });
    },
     },
     mounted() {
        fetch("http://localhost:3000/categoria")
        .then((res) =>res.json())
        .then((res)=>this.categorias=res);
    },
     components: {
     }
 }
 </script>
 <style >
  .producto-relacionado-precio{
        background: orangered;
        color: white;
        text-align: center;
        padding: 10px; 
    }
 </style>