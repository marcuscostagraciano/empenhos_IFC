<script setup>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { LineChart, PieChart } from "echarts/charts";
import {
  DatasetComponent,
  GridComponent,
  LegendComponent,
  TooltipComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { useAppStore } from "../stores/app";

const appStore = useAppStore();

use([
  CanvasRenderer,
  LineChart,
  PieChart,
  LegendComponent,
  TooltipComponent,
  DatasetComponent,
  GridComponent,
]);

provide(THEME_KEY, "default");

const headers = [
  { title: 'Mês', align: 'start', key: 'month' },
  { title: 'Empenhado (R$)', align: 'end', key: 'committed' },
  { title: 'Liquidado (R$)', align: 'end', key: 'liquidated' },
]
</script>

<template>
  <div class="ma-16">
    <TitleSection title="Total de Recursos Empenhados e Liquidados" />
    <div class="chart-dataset">
      <v-chart class="chart" :option="appStore.mainChart" />
    </div>
    <DataframeView :headers="headers" :items="appStore.mainDataframe" />
  </div>
</template>

<style lang="css" scoped>
.chart-dataset {
  height: 400px;
}
</style>
