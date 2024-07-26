import { defineStore } from "pinia";
import { computed, reactive } from "vue";
import AppService from "@/services/app";

export const useAppStore = defineStore("app",
    () => {
        const state = reactive({
            loading: false,
            error: null,
            theme: "light",
            charts: [],
        });
        const isDark = computed(() => state.theme === 'dark');
        const themeColor = computed(() => state.theme);
        const isLoading = computed(() => state.loading);

        const setTheme = (theme) => {
          state.theme = theme;
        }

        const fetchCharts = async () => {
            state.loading = true;
            try {
              state.charts = await AppService.getCharts();
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
            setTheme,
        };
    }
)
