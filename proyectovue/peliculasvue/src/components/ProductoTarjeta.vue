<template>
    <div class="col">
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title"> {{producto.nombre}}</h5>
                <img :src= producto.imagen alt="" width="100%">
                <img :src="`images/${producto.imagen}`" class="img-responsive" 
          height="70" width="90">
                <p class="card-text">{{producto.descripcion}}</p>
                    <div class="producto-relacionado-precio">Precio: {{producto.precio}} BOB</div>
                <div>
                    <div>
                        <div v-for="color of producto.colores" class="color-box"  :style="{'background-color':color }"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
 
 <script>
 export default {
     name: 'productoTarjeta',
     props:["producto"],
     emits:[],
     data(){
         return {
         }
     },
     methods: {
     },
     computed: {
     },
     mounted(){
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