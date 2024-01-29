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
import { ref } from "vue";
import { useCounterStore } from "src/stores/example-store";
import net_import from "src/pythonScripts/bitarray/da_ti.py?url";
export default {
  data() {
    return {
      store: useCounterStore(),
      pyodide: ref(null),
      net_import_: null,
      // Python交互组件
      textInput: "",
      textOutput: "运行结果",
    };
  },
  methods: {
    async runPython() {
      console.log(this.pyodide);
      Promise.resolve().then((res) => {
        this.store.setGlobalLoading(true);
        this.pyodide.runPython(this.textInput);
        this.textOutput = this.pyodide.runPython(this.textInput);
        console.log(this.textOutput);
        this.store.setGlobalLoading(false);
      });
    },
  },

  mounted() {
    Promise.resolve()
      .then((res) => {
        setTimeout(() => {
          this.store.setFooterNote(
            "要使用NumPy库，首先要在Python脚本中编写 import numpy as np。"
          );
          // 加载Python环境
          this.pyodide = this.store.pyodide;
        }, 1000);
      })
      .then((res) => {
        setTimeout(() => {
          this.pyodide.loadPackage("micropip");
        }, 1000);
      })
      .then((res) => {
        setTimeout(() => {
          this.pyodide.loadPackage("bitarray");
        }, 1000);
      })
      .then((res) => {
        setTimeout(() => {
          //读取本地脚本
          fetch(net_import).then((response) => {
            response.text().then((text) => {
              this.net_import_ = text;
              this.textInput = this.net_import_;
            });
          });
        }, 100);
      });
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