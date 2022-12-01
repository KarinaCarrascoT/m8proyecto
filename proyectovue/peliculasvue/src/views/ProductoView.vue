<template>
  <div class="home">
      <ProductoPrincipal :producto=producto :precioEstilos=precioEstilos></ProductoPrincipal>
      <div class="container ">

        <div class="row">
            <h4>Productos relacionados</h4>
        </div>
        <div class="row">
          <ProductoTarjeta class="clic" v-for="productoR of productosRelacionados"  @click="cambiar(productoR.id)" :producto="productoR"></ProductoTarjeta>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import ProductoPrincipal from '@/components/ProductoPrincipal.vue';
import ProductoTarjeta from '@/components/ProductoTarjeta.vue';
  export default {
    name: 'ProductoView',
    data(){
      return {
          productos:[],
          productosRelacionados:[],
          producto:{},
          precioEstilos: "background: orangered; color: white; font-weight: bold"
      }
    },
    methods: {
      getProductos(){
          if(typeof this.$route.params.id == 'undefined')
          {
              axios({
                method: "get",
                url: "http://localhost:4444/Productos"
              })
              .then(response => {
                  this.productos = response.data;
                  this.producto=this.productos[0];
                  this.productosRelacionados=this.productos.filter((x) => x.id!= this.producto.id);
                  console.log(response);
              })
              .catch(e => console.log(e));
 
          }
          else
          {
            axios({
                method: "get",
                url: "http://localhost:4444/Productos"
              })
              .then(response => {
                  this.productos = response.data;
                  this.producto=this.productos.filter((x) => x.id== this.$route.params.id)[0];
                  this.productosRelacionados=this.productos.filter((x) => x.id!= this.$route.params.id);
                  console.log(response);
              })
              .catch(e => console.log(e));
          }
          
      },
      cambiar(idNuevo){
        this.$store.state.cantidad = 1;
        this.$store.state.color = "";
        this.$store.state.botonEstado = true;

        this.producto=this.productos.filter((x) => x.id== idNuevo)[0];
        this.productosRelacionados=this.productos.filter((x) => x.id!= idNuevo);
        this.$router.push({name: 'productoId', params: {id: idNuevo}});
      }
    },
    mounted(){
      this.getProductos()
    },
    components: {
      ProductoPrincipal,ProductoTarjeta
    }
  }
  </script>
  <style>
  .container{
    margin-top: 50px;
  }
  
  .clic{
        cursor: pointer;
    }
  </style>