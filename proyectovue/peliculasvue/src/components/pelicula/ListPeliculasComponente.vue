<template>
    <div>
        <h1>Listado de peliculas en componente</h1>
        <div v-for="c in peliculas" k:ey="c.id">
            <div >Nombre: {{c.nombre}} </div>
            <div >Descripción: {{c.descripcion}} </div>
	    <div >Imagen: {{c.imagen}} </div>
	    <div >Precio: {{c.precio}} </div>
	    <div >Categorías: {{c.categorias}} </div>
	    <div >Horarios: {{c.horarios}} </div>
            <div><button onclick="removePelicula(c.id)">eliminar</button></div>
            <!--{{c.nombre,
            c.descripcion
            }}-->
           <!-- <ul>
                <li
                    v-for="pelicula of peliculas"
                    :class="{ bought: pelicula.bought }"
                    :key="pelicula.id"
                    @click="updatePelicula(pelicula.id)"
                    @dblclick="removePelicula(pelicula.id)"
                >
                    {{ pelicula.nombre,
                    pelicula.descripcion }}
                </li>
            </ul>
            -->
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