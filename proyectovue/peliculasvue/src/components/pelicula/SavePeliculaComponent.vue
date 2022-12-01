<template>
    <update v-bind:update="false" form-title="Registrar"></update>

    <h2>Filtro de precios de peliculas {{textoABuscar}}</h2>
        <form action="">
        <div class="input-group mb-3">
            <input type="text" v-model="textoABuscar" class="form-control" placeholder="Ingrese el precio maximo para filtrar los menores..." >
            <button class="btn btn-outline-secondary" @click.prevent="getMenorPrecio(textoABuscar)">Filtrar</button>

        </div>
   
       </form>
   
    <h2>Listado de pelicula</h2>

    <input type="text" v-model="buscar" class="form-control" placeholder="Escribe para buscar una pelicula....."/>
    
    <div class="row mt-3">
    
        <div class="col-md-4" v-for="item in items" v-bind:key="item.id"> 

            <div class="card mb-3">
                <!--<img class="card-img-top" v-bind:src="'img/' + item.img" v-bind:alt="item.nombre">-->
                <div class="card-body">
                <h3 class="card-title mb-3"><strong>Nombre:</strong>{{ item.nombre }}</h3>
                <p class="card-text"><strong>Descripcion:</strong> {{ item.descripcion }}</p>
                <img v-bind:src="item.imagen " alt="" style="width:100%">
                <!--<p class="card-text"><strong>Imagen:</strong> {{ item.imagen }}</p>-->
                <p class="card-text"><strong>Precio:</strong> {{ item.precio }}</p>
                <p class="card-text"><strong>Categorias:</strong>
                    <div class="col-md-12" v-for="itemCat in item.categorias" v-bind:key="itemCat.id">
                     {{ itemCat }}
                    </div>
                </p>
                <p class="card-text"><strong>Horarios:</strong> 
                    <div class="col-md-12" v-for="itemHor in item.horarios" v-bind:key="itemHor.id">
                     {{ itemHor }}
                    </div>
		<div><button class="btn btn-danger" @click="removePelicula(item.id)">eliminar {{item.id}}</button></div>
    </p>
        
                <button class="btn btn-primary" v-on:click="update =true" @click="getPelicula(item.id)">Actualizar Pelicula {{item.id}}</button>
                </div>
            </div>
        </div>
    </div>
        <!--<div v-for="c in peliculas" k:ey="c.id">
            <div >Nombre: {{c.nombre}} </div>
            <div >Descripcion: {{c.descripcion}} </div>
            <div><button @click="removePelicula(c.id)">eliminar {{c.id}}</button></div>
            
            <button v-on:click="update =true" @click="cargarPelicula(c.id)">Actualizar Pel�cula</button>
             
        </div>-->
        <button class="btn btn-warning" v-on:click="update =false">Crear Pelicula</button>
        <div v-if="update==true">
            <div class="col">
                <div class="card" >
                    <div class="card-body">
                        <h1>ACTUALIZAR PELICULA</h1>
                        <form @submit="sendForm2">
                            <div><label>Nombre: </label></div>
                           <div><input v-model="pelicula.nombre" type="text" ></div> 
                            <div><label>Descripcion: </label></div>
                            <div><input v-model="pelicula.descripcion" type="text" /></div>
                            <!--<div><label>Imagen: </label></div>
                            <input v-model="pelicula.imagen" type="text" />-->
			                <div><label>Precio: </label></div>
                            <div><input v-model="pelicula.precio" type="text" /></div>
			                <div><label>Categorias: </label></div>
                            <div><input v-model="pelicula.categorias" type="text" /></div>
			                <div><label>Horarios: </label></div>
                            <div><input v-model="pelicula.horarios" type="text" /></div>
                            <br>
                            <!--<select  v-model="id">
                                <option v-for="c  in peliculas" ::key="c.id" :value="c.id">
                                    {{c.nombre}}
                                </option>
                            </select>-->
                            <input class="btn btn-primary" type="submit" value="Enviar" @click="getPeliculasRefresh()">
                            <button class="btn btn-danger" v-on:click="update =null">cancelar</button>
                        </form>
                        
                    </div>
                </div>
            </div>
        </div>
 
        <div v-if="update==false">
            <div class="col">
                <div class="card" >
                    <div class="card-body">
                        <h1>REGISTRAR PELiCULA</h1>
                        <form @submit="sendForm">
                            <div><label>Nombre: </label></div>
                           <div><input v-model="pelicula.nombre" type="text" ></div> 
                            <div><label>Descripcion: </label></div>
                            <div><input v-model="pelicula.descripcion" type="text" /></div>
                            <!----><div><label>Imagen: </label></div>
                            <div><input v-model="pelicula.imagen" type="text" placeholder="Inserte la ruta de la imagen en la web" /></div>
			                <div><label>Precio: </label></div>
                            <div><input v-model="pelicula.precio" type="text" /></div>
                            <div> Categorias:</div>
                            <!--<div>Checked Categorias: {{ checkedNames }}</div>
                            <div v-for="c in categorias" k:ey="c.id">
                                <input type="checkbox" :id="c.id" :value=c.nombre v-model="checkedNames">
                                <label :for="c.nombre">{{c.nombre}}</label>
                                 <div >Nombre: {{c.nombre}} </div>
                                <div><button @submit.prevent="agregarCategoriaListaPelicula(c.nombre)">agregar a pelicula</button></div>
                            </div>-->
                            <div><input v-model="pelicula.categorias" type="text" /></div>
			                <div><label>Horarios: </label></div>
                            <div><input v-model="pelicula.horarios" type="text" /></div>
                            <br>
                            <!--<select  v-model="id">
                                <option v-for="c  in peliculas" ::key="c.id" :value="c.id">
                                    {{c.nombre}}
                                </option>
                            </select>-->
                            <div class="col-md-12"> <input class="btn btn-primary" type="submit" value="Enviar" @click=""></div>
                            <br>
                            <div class="col-md-12"><button class="btn btn-danger" v-on:click="update =null">cancelar</button></div> 
                        </form>
                    </div>
            </div>
        </div>
    </div>
</template>
 
 <script>
 import axios from "axios";
 import ListCategoriasComponente from '@/components/categoria/ListCategoriasComponente.vue'
 export default {
    props: {
        update: Boolean,
        formTitle: String,
        peliculaActualizar: [],
        pelicula: {
                nombre:"",
                descripcion:"",
		imagen:"",
		precio:"",
		categorias:[],
        categoriasParaUnaPelicula:[],
		horarios:[],
                textoABuscar: '',
            },         
    },
     data(){
         return {
            update: Boolean,
            peliculas: [],
            pelicula: {
                nombre:"",
                descripcion:"",
                imagen:"",
                precio:"",
                categorias:[],
                horarios:[],
                textoABuscar: '',
            }, 
            peliculaActualizar: [],  
            categoriasParaUnaPelicula:[],  
            buscar: '',       
         };
     },
     methods: {
        sendForm(e){
            e.preventDefault();
            
            console.log(this.pelicula);
            const formData = new FormData();
            
            formData.append("nombre", this.pelicula.nombre);
            formData.append("descripcion", this.pelicula.descripcion);
            formData.append("imagen", this.pelicula.imagen);
            formData.append("precio", this.pelicula.precio);
            formData.append("categorias", this.pelicula.categorias);
            formData.append("horarios", this.pelicula.horarios);	 
            //this.insert(formData);
            this.addPelicula();
        },
        sendForm2(e){
            e.preventDefault();
            
            console.log(this.pelicula);
            const formData = new FormData();

            formData.append("id", this.pelicula.id);
            formData.append("imagen", this.pelicula.imagen);
            formData.append("nombre", this.pelicula.nombre);
            formData.append("descripcion", this.pelicula.descripcion);
            formData.append("precio", this.pelicula.precio);
            formData.append("categorias", this.pelicula.categorias);
            formData.append("horarios", this.pelicula.horarios);
            //this.insert(formData);
            this.guardar(this.pelicula.id);
        },
        insert(formData)
        {
            fetch("http://localhost:3000/pelicula/",{
                method: "POST",
                body: formData,
            })
                .then((res) =>res.json())
                .then((res)=>console.log(res));
        },
        async addPelicula() {
            const res = await axios.post(`http://localhost:3000/pelicula`, {
                nombre: this.pelicula.nombre,
                descripcion: this.pelicula.descripcion, imagen: this.pelicula.imagen ,
            categorias: [this.pelicula.categorias] ,precio: this.pelicula.precio, horarios: [this.pelicula.horarios]
            }); 
            this.peliculas = [...this.peliculas, res.data];
            this.nombre = "";
            this.descripcion = "";
            console.log(this.checkedNames.value);
        },

       async guardar(id){

        axios.patch(`http://localhost:3000/pelicula/${id}`,
            { "nombre": this.pelicula.nombre, "descripcion": this.pelicula.descripcion, "imagen": this.pelicula.imagen ,
            "categorias": [this.pelicula.categorias] ,"precio": this.pelicula.precio, "horarios": [this.pelicula.horarios]}
           // { headers: { 'Content-Type': 'application/json', 'X-CSRF-TOKEN': crsfToken }, }
        ).then((response) => {
            // Code
            console.log("actualizado");
            this.peliculas = [...this.peliculas, res.data];
            this.nombre = "";
            this.descripcion = "";
            getPeliculasRefresh();
        }).catch((error) => {
            // Code
            //console.log(error);
        })
       
        },
        removePelicula(id) {
            axios.delete(`http://localhost:3000/pelicula/${id}`)
            this.peliculas = this.peliculas.filter(pelicula => pelicula.id !== id)
            console.log(pelicula);
        },
        async cargarPelicula(id){
            axios.get(`http://localhost:3000/pelicula/${id}`)
            this.peliculas = this.peliculas.filter(pelicula => pelicula.id !== id)
            return pelicula;
            console.log(pelicula.nombre + pelicula.descripcion);
        },
        getPeliculas() { //id
            axios({
                method: "get",
                //url:  `http://localhost:3000/pelicula/${id}`
                url:  "http://localhost:3000/pelicula/?q="+this.textoABuscar
                //process.env.VUE_APP_RUTA_API+"/tareas/?q="+this.textoABuscar
            })
                .then(response => {
                    this.peliculas = response.data;
                    console.log(response);
                })
                .catch(e => console.log(e));
        },
        getPeliculasRefresh() {
            axios({
                method: "get",
                url:  `http://localhost:3000/pelicula`
                //url: process.env.VUE_APP_RUTA_API+"/tareas/?q="+this.textoABuscar
            })
                .then(response => {
                    this.peliculas = response.data;
                    console.log(response);
                })
                .catch(e => console.log(e));
        },
        getPelicula(id){
            axios({
                method: "get",
                //url: process.env.VUE_APP_RUTA_API+"/tareas/"+this.$route.params.id
                url:  `http://localhost:3000/pelicula/${id}`
            })
            .then(response => {
                this.pelicula = response.data;
            console.log(response);
            })
            .catch(e => console.log(e));
        },
        async getMenorPrecio(precio){
            axios.get(`http://localhost:3000/pelicula`)
            .then(response => {
                    this.peliculas = response.data;
                    console.log(response);
                    this.peliculas = this.peliculas.filter(pelicula => pelicula.precio < precio)
                    return peliculas
                })
                .catch(e => console.log(e));
           ;
            //console.log(pelicula.nombre + pelicula.descripcion);
        },
        agregarCategoriaListaPelicula(categoria){
            categoriasParaUnaPelicula=categoriasParaUnaPelicula.insert(categoria);
            console.log(categoriasParaUnaPelicula);
        }
     },
     computed: {

        items() {
      return this.peliculas.filter(item => {
        return item.nombre.toLowerCase().includes(this.buscar.toLowerCase());
      });
    },
     },
     mounted() {
        fetch("http://localhost:3000/pelicula")
        .then((res) =>res.json())
        .then((res)=>this.peliculas=res);
        fetch("http://localhost:3000/categoria")
        .then((rescat) =>rescat.json())
        .then((rescat)=>this.categorias=rescat);
    },
    
     components: {
        ListCategoriasComponente
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