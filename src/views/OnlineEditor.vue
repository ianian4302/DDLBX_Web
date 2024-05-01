<script setup>
import custom_button from "../components/button.vue";
import { createApp, ref } from "vue";
import {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
} from "@google/generative-ai";

const flag = ref("input from here:\n");
const input_message = ref(`
#include <iostream>
using namespace std;
int main(){
    cout << 1 << endl;
    return 0;
}`);
const compileMarkdown = ref("");
//google generative ai
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
const prmpt =
    "從現在開始你是一個c++的直譯器，你需要針對我給你的語法進行運算，並在print時印出正確的結果，標籤為：input from here:，如果錯誤請統一回答：error，如果有輸出請加上：>>>，如果沒有輸入就輸出空,告訴我錯哪裡\n";

async function generateText() {
    console.log("input_message.value:", input_message.value);
    console.log("prmpt:", prmpt);
    const parts = [{ text: prmpt + flag + input_message.value }]; // 可以根據需要更改文字部分
    const result = await model.generateContent({
        contents: [{ role: "user", parts }],
        generationConfig,
        safetySettings,
    });
    compileMarkdown.value = result.response.text();
}
</script>

<template>
    <hr />
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
    <div>
        <button @click="generateText">生成文字</button>
        <div v-if="generatedText">{{ generatedText }}</div>
    </div>
    <p></p>
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
}
#ouput {
    margin-top: 10px;
    margin-bottom: 10px;
    height: 500px;
    font-size: 20px;
}

body,
#editor {
    margin: 0;
    height: 100%;
    font-family: "Lucida Console", Courier, monospace;
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
</style>
