import { defineStore } from "pinia";
import { computed, reactive } from "vue";
import AppService from "@/services/app";

export const useAppStore = defineStore("app",
    () => {
        const state = reactive({
            loading: false,
            error: null,
            theme: "light",
            datas: {
              mainChart: [],
              globalIndicators: {
                committed: 0,
                settled: 0,
                balance: 0
              }
            },
        });
        const isDark = computed(() => state.theme === 'dark');
        const themeColor = computed(() => state.theme);
        const isLoading = computed(() => state.loading);
        const committed = computed(() => state.datas.globalIndicators.committed);
        const settled = computed(() => state.datas.globalIndicators.settled);
        const balance = computed(() => state.datas.globalIndicators.balance);
        const mainChart = computed(() => state.datas.mainChart[0]);
        const mainDataframe = computed(() => state.datas.mainChart[1]);

        const setTheme = (theme) => {
          state.theme = theme;
        }

        const getCharts = async () => {
            state.loading = true;
            try {
              state.datas = await AppService.getCharts();
            } catch (error) {
              state.error = error;
            } finally {
              state.loading = false;
            }
        }

        return {
            state,
            themeColor,
            isDark,
            isLoading,
            committed,
            settled,
            balance,
            mainChart,
            mainDataframe,
            setTheme,
            getCharts,
        };
    }
)
