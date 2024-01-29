<template>
  <div class="q-pa-md row">
    <div class="q-pa-md q-gutter-sm col">
      <q-btn
        color="white"
        text-color="black"
        label="点击按钮弹出输入框。这个输入框同样可以带校验"
        @click="changeInput('Standard')"
      >
        <q-popup-edit v-model="text" auto-save v-slot="scope">
          <q-input
            v-model="scope.value"
            dense
            autofocus
            counter
            @keyup.enter="scope.set"
            label="带校验的输入框"
            lazy-rules
            :rules="[(val) => (val && val.length > 0) || '此输入框不允许留空']"
          /> </q-popup-edit
      ></q-btn>
    </div>
    <q-separator vertical inset />
    <div class="q-gutter-y-md q-pa-sm col">
      <q-input
        v-model="text"
        label="带校验的输入框"
        :reactive-rules="true"
        :rules="[(val) => (val && val.length > 0) || '此输入框不允许留空']"
        clearable
        dense
      />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useCounterStore } from "src/stores/example-store";

export default {
  setup() {
    const store = useCounterStore();
    setTimeout(() => {
      store.setFooterNote("点击按钮更新输入框中的内容");
    }, 10);

    return {
      store,
      text: ref(""),
      changeInput(t) {
        this.text = t;
      },
    };
  },
};
</script>
