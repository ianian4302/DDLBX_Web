<script setup>
import { ref } from "vue";
import { MdEditor } from "md-editor-v3";
import "md-editor-v3/lib/style.css";

const text = ref("# Hello Editor");
const FilePath = ref("test.txt");
</script>
<script>
export default {
    data() {
        return {
            code: "",
            result: null,
        };
    },
    methods: {
        async sendCode() {
            try {
                const response = await fetch("http://127.0.0.1:5000/compile", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ code: this.code }),
                });
                const data = await response.json();
                this.result = data.result;
            } catch (error) {
                console.error("Error:", error);
            }
        },
    },
};
</script>
<template>
    <div>
        <textarea v-model="code"></textarea>
        <button @click="sendCode">Compile Code</button>
        <div v-if="result">Result: {{ result }}</div>
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
</style>
