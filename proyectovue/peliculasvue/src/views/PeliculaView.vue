<template>
  <div class="home">
    <!--<ListCategorias/>-->
    <SavePeliculaComponent/>
  </div>
</template>

<script>
  //import ListCategorias from '@/components/categoria/ListCategoriasComponente.vue'
//import SaveCategoria from '@/components/categoria/SaveCategoriaComponent.vue'
import SavePeliculaComponent from '@/components/pelicula/SavePeliculaComponent.vue';

export default {
  name: 'PeliculaView',
  components: {
  //ListCategorias,
  //SaveCategoria,
  SavePeliculaComponent
}
}
</script>