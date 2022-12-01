<template>
    <div>
        <h1>Listado de categorias en componente</h1>
        <div v-for="c in categorias" k:ey="c.id">
            <div >Nombre: {{c.nombre}} </div>
            <div >Descripcion: {{c.descripcion}} </div>
            <div><button onclick="removeCategoria(c.id)">eliminar</button></div>
            <!--{{c.nombre,
            c.descripcion
            }}-->
           <!-- <ul>
                <li
                    v-for="categoria of categorias"
                    :class="{ bought: categoria.bought }"
                    :key="categoria.id"
                    @click="updateCategoria(categoria.id)"
                    @dblclick="removeCategoria(categoria.id)"
                >
                    {{ categoria.nombre,
                    categoria.descripcion }}
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
            categorias: []
        };
    },
    mounted() {
        fetch("http://localhost:3000/categoria")
        .then((res) =>res.json())
        .then((res)=>this.categorias=res);
    },
 };   
</script>