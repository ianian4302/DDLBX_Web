<script setup>
import { marked } from "marked";
import { createApp } from "vue";
import { ref } from "vue";
import { GoogleGenerativeAI } from "https://esm.run/@google/generative-ai";

const input_message = ref("");
const compileMarkdown = input_message;

function say(message) {
  alert(message)
}
</script>

<template>
    <span>Multiline message is:</span>
    <p></p>
    <textarea v-model="input_message" placeholder="code input here"></textarea>
    <textarea
        v-model="compileMarkdown"
        placeholder="code onput here"
    ></textarea>
    <p></p>
    <button @click="say('click')">Say</button>
</template>

<style>
body,
#editor {
    margin: 0;
    height: 100%;
    font-family: "Helvetica Neue", Arial, sans-serif;
    color: #333;
}

textarea,
#editor div {
    display: inline-block;
    width: 49%;
    height: 100%;
    vertical-align: top;
    box-sizing: border-box;
    padding: 0 20px;
}

textarea {
    border: none;
    border-right: 1px solid #ccc;
    resize: none;
    outline: none;
    background-color: #f6f6f6;
    font-size: 14px;
    font-family: "Monaco", courier, monospace;
    padding: 20px;
}

code {
    color: #f66;
}
</style>
