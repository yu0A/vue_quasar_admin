<template>
  <div class="q-pa-md">
    <q-table
      class="my-sticky-header-column-table"
      flat
      bordered
      title="Treats"
      :rows="rows"
      :columns="columns"
      row-key="index"
      :pagination-label="setPaginationLabel"
      rows-per-page-label="每页条数："
      :pagination="pagination"
      virtual-scroll
      style="height: 300px"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import { useCounterStore } from "src/stores/example-store";

export default {
  setup() {
    const store = useCounterStore();
    setTimeout(() => {
      store.setFooterNote("通过表格的虚拟滚动特性可以提升页面的速度。在拖拽滚动条时，可以察觉出框架内部对虚拟滚动的优化");
    }, 10);

    const columns = [
      {
        name: "index",
        label: "#",
        field: "index",
      },
      {
        name: "name",
        required: true,
        label: "Dessert (100g serving)",
        align: "left",
        field: (row) => row.name,
        format: (val) => `${val}`,
        sortable: true,
      },
      {
        name: "calories",
        align: "center",
        label: "Calories",
        field: "calories",
        sortable: true,
      },
      { name: "fat", label: "Fat (g)", field: "fat", sortable: true },
      { name: "carbs", label: "Carbs (g)", field: "carbs" },
      { name: "protein", label: "Protein (g)", field: "protein" },
      { name: "sodium", label: "Sodium (mg)", field: "sodium" },
      {
        name: "calcium",
        label: "Calcium (%)",
        field: "calcium",
        sortable: true,
        sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
      },
      {
        name: "iron",
        label: "Iron (%)",
        field: "iron",
        sortable: true,
        sort: (a, b) => parseInt(a, 10) - parseInt(b, 10),
      },
    ];

    const seed = [
      {
        name: "Frozen Yogurt",
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        sodium: 87,
        calcium: "14%",
        iron: "1%",
      },
      {
        name: "Ice cream sandwich",
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
        sodium: 129,
        calcium: "8%",
        iron: "1%",
      },
      {
        name: "Eclair",
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
        sodium: 337,
        calcium: "6%",
        iron: "7%",
      },
      {
        name: "Cupcake",
        calories: 305,
        fat: 3.7,
        carbs: 67,
        protein: 4.3,
        sodium: 413,
        calcium: "3%",
        iron: "8%",
      },
      {
        name: "Gingerbread",
        calories: 356,
        fat: 16.0,
        carbs: 49,
        protein: 3.9,
        sodium: 327,
        calcium: "7%",
        iron: "16%",
      },
      {
        name: "Jelly bean",
        calories: 375,
        fat: 0.0,
        carbs: 94,
        protein: 0.0,
        sodium: 50,
        calcium: "0%",
        iron: "0%",
      },
      {
        name: "Lollipop",
        calories: 392,
        fat: 0.2,
        carbs: 98,
        protein: 0,
        sodium: 38,
        calcium: "0%",
        iron: "2%",
      },
      {
        name: "Honeycomb",
        calories: 408,
        fat: 3.2,
        carbs: 87,
        protein: 6.5,
        sodium: 562,
        calcium: "0%",
        iron: "45%",
      },
      {
        name: "Donut",
        calories: 452,
        fat: 25.0,
        carbs: 51,
        protein: 4.9,
        sodium: 326,
        calcium: "2%",
        iron: "22%",
      },
      {
        name: "KitKat",
        calories: 518,
        fat: 26.0,
        carbs: 65,
        protein: 7,
        sodium: 54,
        calcium: "12%",
        iron: "6%",
      },
    ];

    // we generate lots of rows here
    let rows = [];
    for (let i = 0; i < 1000; i++) {
      rows = rows.concat(seed.slice(0).map((r) => ({ ...r })));
    }
    rows.forEach((row, index) => {
      row.index = index;
    });
    const pagination = {
      sortBy: null, // String, column "name" property value
      descending: false,
      page: 1,
      rowsPerPage: 5, // current rows per page being displayed
    };

    return {
      store,
      text: ref(""),
      changeInput(t) {
        this.text = t;
      },
      columns,
      rows,
      setPaginationLabel(firstRowIndex, endRowIndex, totalRowsNumber) {
        return (
          "第" +
          firstRowIndex +
          " - " +
          endRowIndex +
          "条记录，共" +
          totalRowsNumber +
          "条记录"
        );
      },
      pagination,
    };
  },
};
</script>

<style lang="sass">
.my-sticky-header-column-table
  /* height or max-height is important */
  height: 100%

  /* specifying max-width so the example can
   highlight the sticky column on any browser window */
  max-width: 100%

  td:first-child
    /* bg color is important for td; just specify one */
    background-color: #00b4ff

  tr th
    position: sticky
    /* higher than z-index for td below */
    z-index: 2
    /* bg color is important; just specify one */
    background: #00b4ff

  /* this will be the loading indicator */
  thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
    /* highest z-index */
    z-index: 3
  thead tr:first-child th
    top: 0
    z-index: 1
  tr:first-child th:first-child
    /* highest z-index */
    z-index: 3

  td:first-child
    z-index: 1

  td:first-child, th:first-child
    position: sticky
    left: 0

  /* prevent scrolling behind sticky top row on focus */
  tbody
    /* height of all previous header rows */
    scroll-margin-top: 48px
</style>