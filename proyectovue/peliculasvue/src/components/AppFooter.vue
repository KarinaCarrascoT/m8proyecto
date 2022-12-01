<template>
     <footer :style="`background-color: ${footerColor}`">
      
    </footer>
</template>
  
  <script>
  export default {
      name: 'appFooter',
      props:["footerColor"],
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
    footer {
                
                text-align: center;
                padding: 30px 10px;
                margin-top: 50px;
                min-height: 100px;
                bottom: 0;
            }
  </style>