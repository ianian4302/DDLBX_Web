<script setup>
import { RouterLink, RouterView } from "vue-router";
import Sidebar from "./components/SideBar.vue";
import Test from "./views/Test.vue";
import onlineEditor from "./views/OnlineEditor.vue";
</script>

<template>
    <main>
        <div class="s"><Sidebar /></div>
        <header></header>
        <body>
            <RouterView />
        </body>
    </main>
</template>

<style scoped>
* {
    background: transparent;
}
header {
    z-index: -1;
}
body {
    margin-left: 80px;
}
.s {
    z-index: 1;
}
main {
    display: flex;
    min-height: 100vh;
    /*background: url("./assets/background_2.png") no-repeat;*/
    background-size: cover;
    background-position: center;
    background-blend-mode: multiply;
    background-color: rgba(0, 0, 0, 0);
}

header {
    display: flex;
    justify-content: space-around;
    padding: 1%;
}
.custom-link {
    text-decoration: none;
    color: #333;
    font-size: 1.5rem;
}
.prview {
    display: flex;
    justify-content: space-between;
}
</style>
