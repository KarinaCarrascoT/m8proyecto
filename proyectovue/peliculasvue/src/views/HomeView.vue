<template>
  <div class="home">
    Esto esta en homeView.vue xd
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/categoria/ListCategoriasComponente.vue'
import HelloWorld from '@/components/categoria/ListCategoriasComponente.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
