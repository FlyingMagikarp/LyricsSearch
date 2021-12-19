import { configure } from 'mobx';
import dataStore from "./modules/stores/dataStore";

configure({ enforceActions: 'observed' });


export default class RootStore {

    public static storeName: string = 'rootStore';

    public static getInstance() {
        if (!RootStore.instance) {
            RootStore.instance = new RootStore();
        }
        return RootStore.instance;
    }

    private static instance: RootStore;

    public dataStore: dataStore;

    private constructor() {
        this.dataStore = new dataStore(this);
    }

}