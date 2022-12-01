<template>
     <div class="container">
        <div class="row">
            <h3>{{producto.nombre}}</h3>
        </div>
        <div class="row">
            <div class="col-12 col-sm-6 col-md-4 ">
                <img :src="producto.imagen"
                    alt="" width="100%">
            </div>
            <div class="col-12 col-sm-6  col-md-8">
                <h6 v-html="producto.descripcion"></h6>
                <div class="p-3 mb-2 text-white" :style="`${precioEstilos}`">
                    Precio: {{producto.precio}} BOB
                </div>
                <h5>Color</h5>
                <div>
                    <div v-for="color of producto.colores" class="color-box clic" @click="colorChange(color)" :style="`background: ${color}`"></div>
                </div>
                <h5>Cantidad</h5>
                <div class="quantity">
                    <button  @click="subtract()">-</button> <div>{{this.$store.state.cantidad}}</div> <button  @click="add()">+</button>
                </div>
                <div class="buy-box">
                    <button type="button" class="btn btn-primary" @click="comprar(producto.id)" :disabled=botonEstado>Comprar</button>
                </div>
                
            </div>
        </div>
    </div>
</template>
  
  <script>
  export default {
      name: 'productoPrincipal',
      props:["producto","precioEstilos"],
      emits:[],
      data(){
          return {
            pedido:
            {
                id:null,
                cantidad: 1,
                color:null
            },
          }
      },
      methods: {
        add: function(){
            this.$store.state.cantidad++;
            if(this.$store.state.cantidad>0 && this.$store.state.color!="")
            {
                this.$store.state.botonEstado=false;
            }
        },
        subtract: function(mensaje){
            if(this.$store.state.cantidad>1)
                this.$store.state.cantidad--;
            if(this.$store.state.cantidad==0){
                this.$store.state.botonEstado=true;
            }
            if(this.$store.state.cantidad>0 && this.$store.state.color!="")
            {
                this.$store.state.botonEstado=false;
            }
        },
        colorChange: function(color){
            this.$store.state.color=color;
            alert("Eligío el color: "+color)
            if(this.$store.state.cantidad>0 && this.$store.state.color!="")
            {
                this.$store.state.botonEstado=false;
            }
            
        },
        comprar: function(idProducto){
            if(this.$store.state.cantidad>0){
                this.pedido.id=idProducto;
                this.pedido.color=this.$store.state.color;
                this.pedido.cantidad=this.$store.state.cantidad;
                alert( JSON.stringify(this.pedido));
            }
            
        }
       
      },
      computed: {
            botonEstado(){
                return this.$store.state.botonEstado;
            }
      },
      mounted(){
       
      },
      components: {
      }
  }
  </script>
  <style >
    .color-box {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin: 7px;
        display: inline-block;
    }

    .clic{
        cursor: pointer;
    }

    .quantity button{
        border-radius: 50%;
        display: inline-block;
        width: 30px;
    }
    .quantity div{
        text-align: center;
        min-width: 30px;
        display: inline-block;
        font-weight: bold;
    }
    .buy-box{
        margin: 20px;
    }
    .container{
        margin-top: 50px;
    }
</style>