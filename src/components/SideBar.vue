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
                        <span class="link-name" style="--i: 1"> DashBoard</span>
                    </RouterLink>
                </li>

                <li class="list-item">
                    <a href="#">
                        <i class="bx bx-user"></i>
                        <span class="link-name" style="--i: 2"> Reference</span>
                    </a>
                </li>
                <li class="list-item">
                    <a href="#">
                        <i class="bx bx-message-detail"></i>
                        <span class="link-name" style="--i: 3"> Messages</span>
                    </a>
                </li>
                <li class="list-item">
                    <a href="#">
                        <i class="bx bx-cog"></i>
                        <span class="link-name" style="--i: 4"> Setting</span>
                    </a>
                </li>
                <li class="list-item">
                    <a href="#">
                        <i class="bx bx-help-circle"></i>
                        <span class="link-name" style="--i: 6"> Help</span>
                    </a>
                </li>
                <li class="list-item">
                    <a href="#">
                        <i class="bx bx-help-circle"></i>
                        <span class="link-name" style="--i: 7">
                            File manager</span
                        >
                    </a>
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
body {
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
    color: #fff;
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
    color: #fff;
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
    color: #fff;
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
