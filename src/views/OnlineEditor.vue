<script setup>
import { marked } from "marked";
import { createApp } from "vue";
import { ref } from "vue";
import { GoogleGenerativeAI } from "https://esm.run/@google/generative-ai";

const input_message = ref("");
const compileMarkdown = input_message;

function say(message) {
  alert(message);
}
</script>

<template>
  <hr />
  <!-- <div class="multinle">Multiline message is:</div> -->
  <p></p>
  <textarea
    id="input"
    v-model="input_message"
    placeholder="code input here"
  ></textarea>
  <textarea
    id="ouput"
    v-model="compileMarkdown"
    placeholder="code onput here"
  ></textarea>
  <p></p>
  <a href="javascript: void(0)" class="btn" @click="say('click')">>
    <span>Button</span>
    <svg width="13px" height="10px" viewBox="0 0 13 10">
      <path d="M1,5 L11,5"></path>
      <polyline points="8 1 12 5 8 9"></polyline>
    </svg>
  </a>
</template>

<style>
.multinle {
  margin-top: 3px;
  margin-bottom: 3px;
  font-size: 20px;
  color: #f5f1ed;
}
#input {
  margin-top: 10px;
  margin-bottom: 10px;
  height: 500px;
  font-size: 20px;
  color: #feeeed;
  background-color: #aa7673;
}
#ouput {
  margin-top: 10px;
  margin-bottom: 10px;
  height: 500px;
  font-size: 20px;
  color: #f3e9d3;
  background-color: #d6a184;
}

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
    background: #FFAB9D;
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
