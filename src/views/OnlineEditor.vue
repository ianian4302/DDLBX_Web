<script setup>
import { ref } from "vue";
import { MdEditor } from "md-editor-v3";
import "md-editor-v3/lib/style.css";

const text = ref("# Hello Editor");
function generateText() {
    console.log(text.value);
}
</script>
<template>
    <div class="a">
        <MdEditor v-model="text" />
    </div>
    <div>
        <button @click="generateText">Button</button>
    </div>
</template>

<style>
.a {
    border: 1px solid #000;
    margin: 10px;
}
.md-editor {
    height: 90vh;
    font-family: "Lucida Console", Courier, monospace;
}
.md-editor-toolbar-wrapper {
    height: 0px;
    padding: 0px;
}

body,
#editor {
    height: 100%;
    font-family: "Lucida Console", Courier, monospace;
    color: #333;
    display: inline-block;
    width: 100%;
    height: 100%;
    vertical-align: top;
    box-sizing: border-box;
}

textarea,
#editor div {
    display: inline-block;
    width: 49%;
    height: 100%;
    vertical-align: top;
    box-sizing: border-box;
    padding: 10px 20px;
}
</style>
