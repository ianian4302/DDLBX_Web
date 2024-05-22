<script setup>
import { ref } from "vue";
import { MdEditor } from "md-editor-v3";
import "md-editor-v3/lib/style.css";

const text = ref("# Hello Editor");
</script>
<script>
export default {
    data() {
        return {
            code: 
`
extern fun println(s: Str): Non
extern fun read(): Str

fun main(): Non {
    var s = '123'!
    println(s)!    
}
`,
            result: "Output:\n",
        };
    },
    methods: {
        async sendCode() {
            try {
                const response = await fetch(
                    "http://34.80.112.223:5000/compile",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({ code: this.code }),
                    }
                );
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
    <div class="title">
        <h1 class="Inheader">Input Field</h1>
        <h1 class="Outheader">Output Field</h1>
    </div>
    <div id="editor">
        <textarea v-model="code"></textarea>
        <div v-if="result">{{ result }}</div>
        <hr />
        <button @click="sendCode">Compile Code</button>
    </div>
</template>

<style>
.title {
    display: flex;
    margin-top: 20px;
    margin-bottom: 20px;
    font-size: 20px;
}
.title h1 {
    width: 49%;
    text-align: left;
}
body,
#editor {
    height: 100%;
    font-family: "Lucida Console", Courier, monospace;
    color: #333;
    display: inline-block;
    width: 100%;
    height: 80%;
    vertical-align: top;
    box-sizing: border-box;
}

textarea,
#editor div {
    display: inline-block;
    width: 49%;
    height: 60%;
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
