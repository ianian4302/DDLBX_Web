<script setup>
import { marked } from "marked";
import { createApp, ref } from "vue";
import {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
} from "@google/generative-ai";

const MODEL_NAME = "gemini-1.0-pro";
const API_KEY = "AIzaSyAnpXYIZ4EqRlogVuxIa62_rlGQZPrpT8g";
const genAI = new GoogleGenerativeAI(API_KEY);
const model = genAI.getGenerativeModel({ model: MODEL_NAME });

const generationConfig = {
    temperature: 0.9,
    topK: 1,
    topP: 1,
    maxOutputTokens: 2048,
};

const safetySettings = [
    {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
];

const generatedText = ref("");

async function generateText() {
    const parts = [{ text: "說你好" }]; // 可以根據需要更改文字部分
    const result = await model.generateContent({
        contents: [{ role: "user", parts }],
        generationConfig,
        safetySettings,
    });
    generatedText.value = result.response.text();
}

const input_message = ref("");
const compileMarkdown = ref("");
function say(message) {
    try {
        compileMarkdown = marked(input_message);
        alert(message);
    } catch (e) {
        console.log(e);
    }
}
//test code
const inputText = ref("");
const resultText = ref("");
function handleKeyDown(event) {
    if (event.key === "Enter") {
        addCharacter();
    }
}
function addCharacter() {
    resultText.value += inputText.value;
    inputText.value = ""; // 清空輸入框
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
    <div>
        <button @click="generateText">生成文字</button>
        <div v-if="generatedText">{{ generatedText }}</div>
    </div>
    <div>
        <input type="text" v-model="inputText" @keydown="handleKeyDown" />
        <button @click="addCharacter">加一個字</button>
        <div>{{ resultText }}</div>
    </div>
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
