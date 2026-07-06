import { createSlice } from "@reduxjs/toolkit";

interface AuthState {
    isAuthenticated: boolean;
    accessToken: string | null;
}

const initialState: AuthState = {
    isAuthenticated: false,
    accessToken: null,
};

const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        loginSuccess(state, action) {
            state.isAuthenticated = true;
            state.accessToken = action.payload;

            localStorage.setItem(
                "access_token",
                action.payload
            );
        },

        logout(state) {
            state.isAuthenticated = false;
            state.accessToken = null;

            localStorage.removeItem("access_token");
        },
    },
});

export const {
    loginSuccess,
    logout,
} = authSlice.actions;

export default authSlice.reducer;