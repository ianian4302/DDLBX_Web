<script setup>
</script>

<template>
    <main class="main">
        <div class="row">
            <div class="title-column">
                <h1 class="title">DDLBX</h1>
                <i class="subtitle">A language that: Develop Derictly, Logically and Beyond Xcellently</i>
            </div>
            <button class="button" onclick="window.location.href='https://github.com/fatbrother/DDLBX'">Go To Repo</button>
        </div>
        <div class="divider"></div>
        <div class="info">
            See 
            <RouterLink to="/document">Syntax</RouterLink>
            for more info.
        </div>
        <div class="spacer"></div>
        <div class="info">
            Try it out in
            <RouterLink to="/onlineEditor">DDLBX</RouterLink>
            and see how it works.
        </div>
        <div class="square-decorate" style="--rotate: 43deg; bottom: 0; right: 0"></div>
        <div class="square-decorate" style="--rotate: 76deg; bottom: -100px; right: 200px; width: 200px; height: 200px"></div>
        <div class="square-decorate" style="--rotate: 100deg; bottom: -100px; left: 0px"></div>
        <div class="circle-decorate" style="bottom: 300px; right: 300px; width: 100px; height: 100px"></div>
        <div class="circle-decorate" style="bottom: 450px; right: 270px; width: 50px; height: 50px"></div>
    </main>
</template>

<style>
.main {
    max-width: 1200px;
    padding: 100px 60px;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
}

.title {
    font-size: 80px;
    font-weight: 900;
}

.subtitle {
    font-size: 30px;
    font-weight: bold;
}

.title-column {
    max-width: 550px;
}

.row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.button {
    color: rgb(48, 48, 48);
    padding: 10px 20px;
    border-radius: 5px;
    width: 250px;
    height: 100px;
    font-size: 35px;
    font-weight: 550;
    border: 3px solid rgb(48, 48, 48);
    background-color: rgb(255, 255, 255);
}

.button:hover {
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.divider {
    width: 100%;
    height: 2px;
    margin: 100px 0;
    background-color: rgb(48, 48, 48);
}

.spacer {
    height: 60px;
}

.info {
    font-size: 25px;
    font-weight: bold;
}

.square-decorate {
    position: fixed;
    width: 300px;
    height: 300px;
    background-color: transparent;
    border: 3px solid  black;
    rotate: var(--rotate);
}

.circle-decorate {
    position: fixed;
    width: 300px;
    height: 300px;
    background-color: transparent;
    border: 3px solid  black;
    border-radius: 50%;
}
</style>
