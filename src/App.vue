<script setup>
import { RouterLink, RouterView } from "vue-router";
import Sidebar from "./components/SideBar.vue";
</script>

<template>
    <main>
        <div class="s"><Sidebar /></div>
        <body>
            <RouterView />
        </body>
    </main>
</template>

<style scoped>
* {
    background: transparent;
}

body {
    margin-left: 100px;
    height: 100vh;
    width: 100vw;
}
.s {
    z-index: 1;
}
main {
    display: flex;
    min-height: 100vh;
    background-size: cover;
    background-position: center;
    background-blend-mode: multiply;
    background-color: rgba(0, 0, 0, 0);
}
</style>
