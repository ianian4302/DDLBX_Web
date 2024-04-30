<script>
import Markdown from "vue3-markdown-it";
import 'highlight.js/styles/monokai.css';

export default {
  components: {
    Markdown
  },
  data() {
    return {
      source: ' '
    }
  },
  mounted() {
    this.fetchMarkdown(); // 在組件掛載後執行 fetchMarkdown 方法
  },
  methods: {
    fetchMarkdown() {
      fetch("./test.md") // 發送請求
        .then((res) => res.text()) // 將回應轉為文本格式
        .then((res) => {
          this.source = res; // 將回應設置到 data 中的 source 屬性中，Vue 會自動更新到畫面上
        })
        .catch((error) => {
          console.error('Fetch error:', error);
        });
    },
  },
}
</script>
<template>
    <div class="about">
        
    </div>
    <div>
        <Markdown :source="source" />
    </div>
</template>

<style>
code {
  background-color: #ffffff68 !important; /* 設置背景為透明 */
}
</style>
