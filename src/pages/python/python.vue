<template>
  <div class="q-pa-md row">
    <div class="q-gutter-y-md q-pa-sm col">
      <q-input v-model="text" label="输入Python脚本" 
        dense/>

      <q-separator vertical inset />
      <div class="q-pa-md q-gutter-sm col">
        <q-btn
          color="white"
          text-color="black"
          label="执行"
          @click="runPython"
        />
      </div>
      <q-separator vertical inset />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useCounterStore } from "src/stores/example-store";

export default {
  setup() {
    const store = useCounterStore();
    let pyodide = ref(null);
    setTimeout(() => {
      store.setFooterNote("执行Python代码");
    // 加载Python环境
      pyodide = store.pyodide;
    }, 10);

    // Python交互组件
    let text = ref("");

    return {
      pyodide,
      store,
      text,
      changeInput(t) {
        this.text = t;
      },
      async runPython() {
        let result = pyodide.runPython(text.value);
        console.log(result);
        setTimeout(() => {
          store.setFooterNote(result);
        }, 10);
      },
    };
  },
};
</script>
