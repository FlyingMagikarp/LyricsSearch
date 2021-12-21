import React from "react";
import ReactDOM from 'react-dom';
import Main from './modules/Main'
import RootStore from "./rootStore";

const rootStore = RootStore.getInstance();

export const StoreContext = React.createContext<RootStore>(rootStore);

function startApplication() {

    ReactDOM.render(
        <>
            <Main/>
        </>,
        document.getElementById('rootApp')
    );
}

startApplication();