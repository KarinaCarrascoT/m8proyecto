<template>
    <div class="home">
      <!--<ListHorarios/>-->
      <SaveHorarioComponent/>
    </div>
  </template>
  
  <script>
    //import ListHorarios from '@/components/horario/ListhorariosComponente.vue'
   // import Savehorario from '@/components/horario/SavehorarioComponent.vue'
import SaveHorarioComponent from '@/components/horario/SaveHorarioComponent.vue';
  
  export default {
    name: 'horarioView',
    components: {
    //Listhorarios,
    //Savehorario,
    SaveHorarioComponent
}
  }
  </script>