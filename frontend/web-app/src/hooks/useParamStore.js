import { create } from "zustand"

const initialState = {
    pageNumber: 1,
    pageSize: 12,
    pageCount: 1,
    searchTerm: '',
    searchValue: '',
    orderBy: 'make',
    filterBy: 'live',
    seller: undefined,
    winner: undefined
}

export const useParamsStore = create()((set) => ({
    ...initialState,

    setParams: (newParams) => {
        set((state) => {
            if (newParams.pageNumber) {
                return {...state, pageNumber: newParams.pageNumber}
            } else {
                return {...state, ...newParams, pageNumber: 1}
            }
        })
    },

    reset: () => set(initialState),

    setSearchValue: (value) => {
        set({searchValue: value})
    }
}))