<script setup>
import { MdPreview, MdCatalog } from "md-editor-v3";

const id = "preview-only";

</script>
<template>
    <MdPreview :editorId="id" :modelValue="source" />
</template>

<script>
export default {
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
            fetch("./syntex.md") // 發送請求
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
    background-color: transparent;
}
</style>
