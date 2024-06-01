import { create } from 'zustand';

type UIStore = {
  menuItem: string;
  darkMode: boolean;
  theme?: string;
  setMenuItem: (menuItem: string) => void;
  setDarkMode: (darkMode: boolean) => void;
};

export const useUIStore = create<UIStore>((set) => ({
  menuItem: 'dashboard',
  darkMode: false,
  theme: undefined,
  setDarkMode: (darkMode: boolean) => {
    if (darkMode) {
      set({ theme: 'dark' });
    } else {
      set({ theme: 'light' });
    }
    set({ darkMode });
  },
  setMenuItem: (menuItem: string) => {
    set({ menuItem });
  },
}));
