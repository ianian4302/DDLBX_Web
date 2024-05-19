<template>
    <MdPreview :editorId="id" :modelValue="source" />
</template>

<script setup>
import { ref } from "vue";
import { MdPreview, MdCatalog } from "md-editor-v3";
import Markdown from "vue3-markdown-it";

const id = "preview-only";
const text = ref("# Hello Editor");
const scrollElement = document.documentElement;
</script>

<script>
export default {
    components: {
        Markdown,
    },
    data() {
        return {
            source: " ",
        };
    },
    mounted() {
        this.fetchMarkdown(); // 在組件掛載後執行 fetchMarkdown 方法
    },
    methods: {
        fetchMarkdown() {
            fetch("./contribute.md") // 發送請求
                .then((res) => res.text()) // 將回應轉為文本格式
                .then((res) => {
                    this.source = res; // 將回應設置到 data 中的 source 屬性中，Vue 會自動更新到畫面上
                })
                .catch((error) => {
                    console.error("Fetch error:", error);
                });
        },
    },
};
</script>

<style>
.md-editor {
    height: 100vh;
    background-color: transparent;
}
</style>
