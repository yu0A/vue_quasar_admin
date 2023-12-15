<template>
  <div class="q-pa-md row self-center full-width no-outline">
    <div class="q-pa-md q-gutter-sm col">
      <q-btn color="white" text-color="black" label="执行" @click="runPython" />
    </div>
  </div>
  <q-separator inset />
  <div class="q-pa-md row self-center full-width full-height no-outline">
    <div class="q-gutter-y-md q-pa-sm col">
      <q-input v-model="textInput" label="输入Python脚本" type="textarea" filled style="height: 70vh" />
    </div>
    <q-separator vertical inset />
    <div class="q-gutter-y-md q-pa-sm col">
      <q-field type="textarea" class="full-height" filled>
        <div style="height: 70vh">{{ textOutput }}</div>
      </q-field>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useCounterStore } from "src/stores/example-store";
import netImportUrl from "src/pythonScripts/net_import.py?url";

export default {
  setup() {
    const store = useCounterStore();
    let pyodide = ref(null);
    let netImport = null;

    setTimeout(() => {
      store.setFooterNote(
        "要使用Python面向对象编程，首先要在脚本中定义类，再创建对象，然后再运行相关的逻辑。"
      );
      // 加载Python环境
      pyodide = store.pyodide;
      // console.log(pyodide)
    }, 5000);

    onMounted(async () => {
      //读取本地脚本
      netImport = await (await fetch(netImportUrl)).text();
      textInput.value = netImport;
    });
    // Python交互组件
    let textInput = ref("");
    let textOutput = ref("运行结果");

    return {
      netImport,
      pyodide,
      store,
      textInput,
      textOutput,
      async runPython() {
        console.log(pyodide)
        await pyodide.loadPackage("micropip");
        await pyodide.loadPackage("numpy")

        store.setGlobalLoading(true);
        pyodide.runPython(textInput.value);
        textOutput.value = pyodide.runPython(textInput.value);
        console.log(textOutput.value);
        store.setGlobalLoading(false);
      },
    };
  },
};
</script>
