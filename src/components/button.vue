<script setup></script>
<template>
    <a href="javascript: void(0)" class="btn" @click="say('click')"
        >>
        <span>Button</span>
        <svg width="13px" height="10px" viewBox="0 0 13 10">
            <path d="M1,5 L11,5"></path>
            <polyline points="8 1 12 5 8 9"></polyline>
        </svg>
    </a>
</template>
<style>
.btn {
    position: relative;
    color: #111111;
    font-size: 1rem;
    text-transform: uppercase;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    transition: all 0.2s ease;
    padding: 12px 20px;
    display: inline-flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.btn:before {
    content: "";
    position: absolute;
    top: -2;
    left: 0;
    display: block;
    border-radius: 28px;
    background: rgba(255, 171, 157, 0.5);
    width: 56px;
    height: 56px;
    transition: all 0.3s ease;
}
.btn span {
    position: relative;
    z-index: 1;
}
.btn svg {
    position: relative;
    top: 0;
    margin-left: 10px;
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke: #111111;
    stroke-width: 2;
    transform: translateX(-5px);
    transition: all 0.3s ease;
}
.btn:hover:before {
    width: 100%;
    background: #ffab9d;
}
.btn:hover svg {
    transform: translateX(0);
}
.btn:hover,
.btn:focus {
    color: #111111;
}
.btn:active {
    color: #111111;
    transform: scale(0.96);
}
</style>
