<template>
    <div class="home">
      <!--<ListCategorias/>-->
      <SaveCategoriaComponent/>
    </div>
  </template>
  
  <script>
    //import ListCategorias from '@/components/categoria/ListCategoriasComponente.vue'
    import SaveCategoria from '@/components/categoria/SaveCategoriaComponent.vue'
import SaveCategoriaComponent from '@/components/categoria/SaveCategoriaComponent.vue';
  
  export default {
    name: 'CategoriaView',
    components: {
    //ListCategorias,
    SaveCategoria,
    SaveCategoriaComponent
}
  }
  </script>