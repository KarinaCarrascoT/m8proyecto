<template>
    <div>
        <h1>Listado de peliculas en componente</h1>
        <div v-for="p in peliculas" k:ey="c.id">
            <div >Nombre: {{p.nombre}} </div>
            <div >Descripcion: {{p.descripcion}} </div>
            <!--{{c.nombre,
            c.descripcion
            }}-->
        </div>
    </div>
</template>

<script>
 export default{
    data(){
        return {
            peliculas: []
        };
    },
    mounted() {
        fetch("http://localhost:3000/pelicula")
        .then((res) =>res.json())
        .then((res)=>this.peliculas=res);
    },
 };   
</script>