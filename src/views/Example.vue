<template>
    <div class="out">
        <div v-for="(item, index) in items" :key="index">
            <h2>{{ item.title }}</h2>
            <MdPreview
                :editorId="`preview-${index}`"
                :modelValue="item.source"
            />
            <hr class="divider" />
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { MdPreview } from "md-editor-v3";

// 定義 items 為一個可響應的數組，包含每個文本框的標題和內容
const items = ref([
    { title: "Fibonacci", source: "" },
    { title: "Hello World", source: "" },
    { title: "Loop", source: "" },
    { title: "Method", source: "" },
    { title: "Polymorphism", source: "" },
    { title: "Simple Object", source: "" },
    { title: "Simple Statement", source: "" },
    { title: "Template", source: "" },
    { title: "Trait", source: "" },
]);

// 定義 fetchMarkdown 函數來加載 Markdown 文件
const fetchMarkdown = (index, url) => {
    fetch(url) // 發送請求
        .then((res) => res.text()) // 將回應轉為文本格式
        .then((res) => {
            items.value[index].source = res; // 更新對應索引的文本框內容
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
};

// 組件掛載後加載每個文本框的內容
fetchMarkdown(0, "./example/fibonacci.md");
fetchMarkdown(1, "./example/hello_world.md");
fetchMarkdown(2, "./example/loop.md");
fetchMarkdown(3, "./example/method.md");
fetchMarkdown(4, "./example/polymorphism.md");
fetchMarkdown(5, "./example/simple_object.md");
fetchMarkdown(6, "./example/simple_stmt.md");
fetchMarkdown(7, "./example/template.md");
fetchMarkdown(8, "./example/trait.md");
</script>

<style>
.md-editor {
    height: 100%;
    background-color: transparent;
}
h2 {
    font-size: 2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}
.out {
    gap: 1rem;
    padding: 1rem;
}
</style>
