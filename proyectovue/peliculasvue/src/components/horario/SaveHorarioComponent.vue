<template>
    <update v-bind:update="false" form-title="Registrar"></update>
    <h1>Listado de horarios</h1>

    <input type="text" v-model="buscar" class="form-control" placeholder="Ingerse el horario que desea buscar. Ejemplo: 08:00"/>
    
    <div class="row mt-3">
    
        <div class="col-md-4" v-for="item in items" v-bind:key="item.id"> 

            <div class="card mb-3">
                <!--<img class="card-img-top" v-bind:src="'img/' + item.img" v-bind:alt="item.hora">-->
                <div class="card-body">
                <h3 class="card-title mb-3"><strong>Hora:</strong>{{ item.hora }}</h3>
                <div><button @click="removehorario(item.id)">eliminar {{item.id}}</button></div>
                <button v-on:click="update =true" @click="gethorario(item.id)">Actualizar horario {{item.id}}</button>
                </div>
            </div>
        </div>
    </div>
        <!--<div v-for="c in horarios" k:ey="c.id">
            <div >Hora: {{c.hora}} </div>
            <div >Hora: {{c.hora}} </div>
            <div><button @click="removehorario(c.id)">eliminar {{c.id}}</button></div>
            
            <button v-on:click="update =true" @click="cargarhorario(c.id)">Actualizar horario</button>
             
        </div>-->
        <button v-on:click="update =false">Crear horario</button>
        <div v-if="update==true">
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h1>ACTUALIZAR horario</h1>
                        <form @submit="sendForm2">
                            <label>Hora: </label>
                            <input v-model="horario.hora" type="text" >
                           
                            <!--<select  v-model="id">
                                <option v-for="c  in horarios" ::key="c.id" :value="c.id">
                                    {{c.hora}}
                                </option>
                            </select>-->
                            <input type="submit" value="Enviar" @click="gethorariosRefresh()">
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
                        <h1>REGISTRAR horario</h1>
                        <form @submit="sendForm">
                            <label>Hora:</label>
                            <input v-model="horario.hora" type="text" />
                           
                            <!--<select  v-model="id">
                                <option v-for="c  in horarios" ::key="c.id" :value="c.id">
                                    {{c.hora}}
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
        horarioActualizar: [],
        horario: {
                hora:"",
                hora:"",
                textoABuscar: '',
            },         
    },
     data(){
         return {
            update: Boolean,
            horarios: [],
            horario: {
                hora:"",
                textoABuscar: '',
            }, 
            horarioActualizar: [],    
            buscar: '',       
         };
     },
     methods: {
        sendForm(e){
            e.preventDefault();
            
            console.log(this.horario);
            const formData = new FormData();
            
            formData.append("hora", this.horario.hora);
            formData.append("hora", this.horario.hora);

            //this.insert(formData);
            this.addhorario();
        },
        sendForm2(e){
            e.preventDefault();
            
            console.log(this.horario);
            const formData = new FormData();

            formData.append("id", this.horario.id);
            formData.append("hora", this.horario.hora);

            //this.insert(formData);
            this.guardar(this.horario.id);
        },
        insert(formData)
        {
            fetch("http://localhost:3000/horario/",{
                method: "POST",
                body: formData,
            })
                .then((res) =>res.json())
                .then((res)=>console.log(res));
        },
        async addhorario() {
            const res = await axios.post(`http://localhost:3000/horario`, {
                hora: this.horario.hora,
            });
            this.horarios = [...this.horarios, res.data];
            this.hora = "";
        },

       async guardar(id){

        axios.patch(`http://localhost:3000/horario/${id}`,
            { "hora": this.horario.hora, "hora": this.horario.hora }
           // { headers: { 'Content-Type': 'application/json', 'X-CSRF-TOKEN': crsfToken }, }
        ).then((response) => {
            // Code
            console.log("actualizado");
            this.horarios = [...this.horarios, res.data];
            this.hora = "";
            gethorariosRefresh();
        }).catch((error) => {
            // Code
            //console.log(error);
        })
       
        },
        removehorario(id) {
            axios.delete(`http://localhost:3000/horario/${id}`)
            this.horarios = this.horarios.filter(horario => horario.id !== id)
            console.log(horario);
        },
        async cargarhorario(id){
            axios.get(`http://localhost:3000/horario/${id}`)
            this.horarios = this.horarios.filter(horario => horario.id !== id)
            return horario;
            console.log(horario.hora + horario.hora);
        },
        getHorarios(id) { //no da
            axios({
                method: "get",
                url:  `http://localhost:3000/horario/${id}`
                //process.env.VUE_APP_RUTA_API+"/tareas/?q="+this.textoABuscar
            })
                .then(response => {
                    this.horarios = response.data;
                    console.log(response);
                })
                .catch(e => console.log(e));
        },
        gethorariosRefresh() {
            axios({
                method: "get",
                url:  `http://localhost:3000/horario`
                //url: process.env.VUE_APP_RUTA_API+"/tareas/?q="+this.textoABuscar
            })
                .then(response => {
                    this.horarios = response.data;
                    console.log(response);
                })
                .catch(e => console.log(e));
        },
        gethorario(id){
            axios({
                method: "get",
                //url: process.env.VUE_APP_RUTA_API+"/tareas/"+this.$route.params.id
                url:  `http://localhost:3000/horario/${id}`
            })
            .then(response => {
                this.horario = response.data;
            console.log(response);
            })
            .catch(e => console.log(e));
        },
     },
     computed: {

        items() {
      return this.horarios.filter(item => {
        return item.hora.toLowerCase().includes(this.buscar.toLowerCase());
      });
    },
     },
     mounted() {
        fetch("http://localhost:3000/horario")
        .then((res) =>res.json())
        .then((res)=>this.horarios=res);
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