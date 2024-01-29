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
import pythonFileUrl from "src/pythonScripts/test.py?url";
import runPythonFileUrl from "src/pythonScripts/run_test.py?url";

export default {
  setup() {
    const store = useCounterStore();
    let pyodide = ref(null);
    setTimeout(() => {
      store.setFooterNote(
        "直接在浏览器中读取并运行Python脚本。第一个Python脚本用于导入函数，第二个Python脚本用于按照程序调用已导入的函数"
      );
      // 加载Python环境
      pyodide = store.pyodide;
    }, 10);

    onMounted(async () => {
      //读取本地脚本
      textInput.value = await (await fetch(pythonFileUrl)).text();
    });
    // Python交互组件
    let textInput = ref("");
    let textOutput = ref("运行结果");

    return {
      pyodide,
      store,
      textInput,
      textOutput,
      async runPython() {
        store.setGlobalLoading(true);
        textOutput.value = pyodide.runPython(textInput.value);
        textOutput.value = pyodide.runPython(
          await (await fetch(runPythonFileUrl)).text()
        );
        console.log(textOutput.value);
        store.setGlobalLoading(false);
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