<template>
  <div class="q-pa-md row self-center full-width no-outline">
    <div class="q-pa-md q-gutter-sm col">
      <q-btn color="white" text-color="black" label="执行" @click="runPython" />
    </div>
  </div>
  <q-separator inset />
  <div class="q-pa-md row self-center full-width full-height no-outline">
    <div class="q-gutter-y-md q-pa-sm col">
      <q-input
        v-model="textInput"
        label="输入Python脚本"
        filled
        class="change-input-height wrap"
        type="textarea"
      />
    </div>
    <q-separator vertical inset />
    <div class="q-gutter-y-md q-pa-sm col">
      <q-input
        v-model="textOutput"
        label="输出结果"
        filled
        class="change-input-height wrap"
        type="textarea"
        readonly
      />
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
    onMounted(async () => {
      setTimeout(() => {
        store.setFooterNote(
          "Python答题页面分为左右两部分，左侧输入Python代码，右侧显示Python执行结果。点击执行按钮后，右侧的结果同步刷新"
        );
        // 加载Python环境
        pyodide = store.pyodide;
      }, 10);
    });

    // Python交互组件
    let textInput = ref("a=1+20;a");
    let textOutput = ref("运行结果");

    return {
      pyodide,
      store,
      textInput,
      textOutput,
      async runPython() {
        textOutput.value = pyodide.runPython(textInput.value);
        console.log(textOutput.value);
      },
    };
  },
};
</script>
<style scoped>
::v-deep div.q-field__control-container.col.relative-position.row.no-wrap.q-anchor--skip {
  height: 70vh;
}
::v-deep div.q-field__control-container.col.relative-position.row.no-wrap.q-anchor--skip > div.q-field__control.relative-position.row.no-wrap {
  height: 70vh;
}
</style>