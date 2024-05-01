<script setup>
import { RouterLink, RouterView } from "vue-router";
import Sidebar from "./components/SideBar.vue";

</script>

<template>
    <main>
        <Sidebar />

        <header>
            <RouterLink class="custom-link" to="/">Home</RouterLink>
            <RouterLink class="custom-link" to="/about">About</RouterLink>
            <RouterLink class="custom-link" to="/onlineEditor">Leetcode</RouterLink>
            
        </header>
        <body>
            <RouterView />
            <!-- <Test/> -->
        </body>
    </main>
</template>

<style scoped>
* {
    background: transparent;
}
body {
    margin-left: 100px;
}
main {
    min-height: 100vh;
    background: url("./assets/background_2.png") no-repeat;
    background-size: cover;
    background-position: center;
    background-blend-mode: multiply;
    background-color: rgba(0, 0, 0, 0.4);
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
</style>
