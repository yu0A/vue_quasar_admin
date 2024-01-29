<template>
  <div class="q-pa-md row">
      <div class="q-pa-md q-gutter-sm col">
        <q-btn color="white" text-color="black" label="Standard" @click="changeInput('Standard')"/>
        <q-btn color="primary" label="Primary"  @click="changeInput('Primary')"/>
        <q-btn color="secondary" label="Secondary"  @click="changeInput('Secondary')"/>
        <q-btn color="amber" glossy label="Amber"  @click="changeInput('Amber')"/>
        <q-btn color="brown-5" label="Brown 5"  @click="changeInput('Brown')"/>
        <q-btn color="deep-orange" glossy label="Deep Orange"  @click="changeInput('Deep Orange')"/>
        <q-btn color="purple" label="Purple"  @click="changeInput('Purple')"/>
        <q-btn color="black" label="Black"  @click="changeInput('Black')"/>
      </div>
      <q-separator vertical inset />
      <div class="q-gutter-y-md q-pa-sm col">
        <q-input v-model="text" label="姓名" />

        <q-input filled v-model="text" label="年龄" />
        <q-separator vertical inset />

        <q-input outlined v-model="text" label="账号" />

        <q-input standout v-model="text" label="密码" />

        <q-input standout="bg-teal text-white" v-model="text" label="性别" />

        <q-input borderless v-model="text" label="生日" />

        <q-input rounded filled v-model="text" label="星座" />

        <q-input rounded outlined v-model="text" label="血型" />

        <q-input rounded standout v-model="text" label="手机号" />

        <q-input square filled v-model="text" label="安全问题" />

        <q-input square outlined v-model="text" label="账号类型" />

        <q-input square standout v-model="text" label="备注" />

        <q-separator vertical inset />
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
      store.setFooterNote(
        "点击按钮更新输入框中的内容"
      );
    }, 10);

    return {
      store,
      text: ref(""),
      changeInput(t){
        this.text = t;
      },
    };
  },
};
</script>
