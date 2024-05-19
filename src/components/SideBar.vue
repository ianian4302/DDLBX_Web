<script setup>
import { ref } from "vue";

const sidebarActive = ref(false);
const toggleSidebar = () => {
    sidebarActive.value = !sidebarActive.value;
};
</script>
<template>
    <head>
        <link
            href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css"
            rel="stylesheet"
        />
    </head>

    <body>
        <nav class="sidebar" :class="{ active: sidebarActive }">
            <div class="logo-menu">
                <h2 class="logo">DDLBX</h2>
                <i class="bx bx-menu toggle-btn" @click="toggleSidebar"></i>
            </div>
            <ul class="list">
                <li class="list-item active">
                    <RouterLink to="/">
                        <i class="bx bx-grid-alt"></i>
                        <span class="link-name" style="--i: 1"> Main</span>
                    </RouterLink>
                </li>

                <li class="list-item">
                    <RouterLink to="/document">
                        <i class="bx bxs-book-open"></i>
                        <span class="link-name" style="--i: 2"> Document</span>
                    </RouterLink>
                </li>
                <li class="list-item">
                    <RouterLink to="/onlineEditor">
                        <i class="bx bx-code-block"></i>
                        <span class="link-name" style="--i: 3">
                            Online Compiler</span
                        >
                    </RouterLink>
                </li>
                <li class="list-item">
                    <RouterLink to="/contribute">
                        <i class="bx bx-donate-heart"></i>
                        <span class="link-name" style="--i: 4">
                            Contribute</span
                        >
                    </RouterLink>
                </li>
                <li class="list-item">
                    <RouterLink to="/test">
                        <i class="bx bx-cog"></i>
                        <span class="link-name" style="--i: 4"> Test</span>
                    </RouterLink>
                </li>
            </ul>
        </nav>
    </body>
</template>
<style>
* {
    font-family: "Poppins", sans-serif;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
.sidebar {
    position: fixed;
    height: 100%;
    width: 80px;
    background: transparent;
    backdrop-filter: blur(2px);
    border-right: 2px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 0 10px rgba(0, 0, 0, 1);
    padding: 6px 14px;
    transition: 0.5s;
}
.sidebar.active {
    width: 260px;
}

.sidebar .logo-menu {
    display: flex;
    align-items: center;
    width: 100%;
    height: 70px;
}
.sidebar .logo-menu .logo {
    caret-color: transparent;
    font-size: 25px;
    color: #000000;
    pointer-events: none;
    opacity: 0;
    transition: 0.3s;
}
.sidebar.active .logo-menu .logo {
    opacity: 1;
    transition-delay: 0.2s;
}
.sidebar .logo-menu .toggle-btn {
    caret-color: transparent;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 40px;
    text-align: center;
    color: #000000;
    line-height: 40px;
    font-size: 22px;
    cursor: pointer;
    transition: 0.5s;
}
.sidebar.active .logo-menu .toggle-btn {
    left: 90%;
}
.sidebar .list {
    margin-top: 10px;
}
.list .list-item {
    list-style: none;
    width: 100%;
    height: 50px;
    margin: 5px 0;
    line-height: 50px;
}
.list .list-item a {
    display: flex;
    align-items: center;
    font-size: 18px;
    color: #000000;
    text-decoration: none;
    border-radius: 6px;
    white-space: nowrap;
    transition: all 0.5s ease;
}
.list .list-item:hover a {
    background: rgba(255, 255, 255, 0.2);
}
.list .list-item a i {
    min-width: 50px;
    height: 50px;
    text-align: center;
    line-height: 50px;
}

.sidebar .link-name {
    opacity: 0;
    pointer-events: none;
    transition: 0.3s;
}
.sidebar.active .link-name {
    opacity: 1;
    pointer-events: auto;
    transition-delay: calc(0.05s * var(--i));
}
</style>
<script></script>
