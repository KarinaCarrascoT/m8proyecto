<template>
    <div>
        <h1>Listado de horarios en componente</h1>
        <div v-for="c in horarios" k:ey="c.id">
            <div >Nombre: {{c.nombre}} </div>
            <div >Descripción: {{c.descripcion}} </div>
            <div><button onclick="removehorario(c.id)">eliminar</button></div>
            <!--{{c.nombre,
            c.descripcion
            }}-->
           <!-- <ul>
                <li
                    v-for="horario of horarios"
                    :class="{ bought: horario.bought }"
                    :key="horario.id"
                    @click="updatehorario(horario.id)"
                    @dblclick="removehorario(horario.id)"
                >
                    {{ horario.nombre,
                    horario.descripcion }}
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
            horarios: []
        };
    },
    mounted() {
        fetch("http://localhost:3000/horario")
        .then((res) =>res.json())
        .then((res)=>this.horarios=res);
    },
 };   
</script>