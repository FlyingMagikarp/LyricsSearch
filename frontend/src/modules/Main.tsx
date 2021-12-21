import React, {useContext, useEffect, useState} from 'react';
import {observer} from "mobx-react-lite";
import {Grid} from "@material-ui/core";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import InputBase from "@material-ui/core/InputBase";
import IconButton from "@material-ui/core/IconButton";
import SearchIcon from '@mui/icons-material/Search';
import createStyles from "@material-ui/core/styles/createStyles";
import makeStyles from "@material-ui/core/styles/makeStyles";
import Button from '@mui/material/Button';
import {StoreContext} from "../index";
import MenuItem from "@material-ui/core/MenuItem";
import Constants from "../util/Constants";
import Select from "@material-ui/core/Select";
import Song from "./model/song";
import CircularProgress from "@material-ui/core/CircularProgress";
import Box from "@material-ui/core/Box";
import Modal from "@material-ui/core/Modal";
import TableContainer from "@material-ui/core/TableContainer";
import Table from "@material-ui/core/Table";
import TableCell from "@material-ui/core/TableCell";
import TableRow from "@material-ui/core/TableRow";
import TableHead from "@material-ui/core/TableHead";
import TableBody from "@material-ui/core/TableBody";

export const useStyles = makeStyles(() => createStyles({
    searchPaper: {
        p: '2px 4px',
        display: 'flex',
        alignItems: 'center',
        width: 400
    },
    searchPaperSmaller: {
        p: '2px 4px',
        display: 'flex',
        alignItems: 'center',
        width: 190
    },
    searchInputBase: {
        ml: 1,
        flex: 1
    },
    searchIconButton: {
        p: '10px'
    },
    genreSelect: {
        width: 170
    },
    modalBox: {
        position: 'absolute' as 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        backgroundColor: 'white',
        border: '2px solid #000',
        boxShadow: '24',
        p: 4,
        padding: 10
    },
    modalDescription: {
        mt: 2,
        height: '400px',
        overflowY: 'scroll',
        overflowX: 'scroll'
    },
    table: {
        minWidth: 650
    },
    tableRow: {

    }

}));

const Main = observer(() => {
    const {dataStore} = useContext(StoreContext);
    const classes = useStyles();

    const [genreIsAnd, setGenreIsAnd] = useState(true);
    const [artistIsAnd, setArtistIsAnd] = useState(true);
    const [searchTerm, setSearchTerm] = useState("");
    const [artistTerm, setArtistTerm] = useState("");
    const [genreTerm, setGenreTerm] = useState<any>("Any");

    const [songs, setSongs] = useState([] as Song[]);

    const [currentSong, setCurrentSong] = useState<Song>(new Song());
    const [isLoading, setIsLoading] = useState(false);


    useEffect(() => {
        setGenreIsAnd(dataStore.genreIsAnd);
        setArtistIsAnd(dataStore.artistIsAnd);
    }, [dataStore]);

    const handleSearchTermChange = (newTerm:string) => {
        setSearchTerm(newTerm);
        dataStore.updateSearchTerm(newTerm)
    };

    const handleArtistTermChange = (newTerm:string) => {
        setArtistTerm(newTerm);
        dataStore.updateArtistTerm(newTerm);
    };

    const handleSearch = async () => {
        setIsLoading(true);
        setSongs(await dataStore.performSearch());
        setIsLoading(false);
    };

    //modal state
    const [open, setOpen] = React.useState(false);
    const handleClose = () => setOpen(false);
    const handleOpen = (song:Song) => {
        // set data for display
        setCurrentSong(song);
        setOpen(true);
    };

    return (
        <Grid container direction={"column"} justifyContent={"center"} alignContent={"center"} spacing={2}>
            <Grid item>
                <Typography variant="h2" color="inherit" component="div">
                    Lyrics Search
                </Typography>
                <Grid container direction={"column"} spacing={1}>
                    <Grid item>
                        <Paper component="form" className={classes.searchPaper}>
                            <InputBase
                                placeholder="Search Lyrics"
                                inputProps={{ 'aria-label': 'search google maps' }}
                                className={classes.searchInputBase}
                                onChange={(event) => {handleSearchTermChange(event.target.value)}}
                            />
                            <IconButton aria-label="search" onClick={handleSearch} className={classes.searchIconButton}>
                                <SearchIcon/>
                            </IconButton>
                        </Paper>
                    </Grid>
                    <Grid item>
                        <Paper component="form" className={classes.searchPaper}>
                            <Button variant={"outlined"} aria-label="artist" className={classes.searchIconButton}
                            onClick={() => {dataStore.toggleArtistIsAnd(); setArtistIsAnd(!artistIsAnd)}}>
                                {artistIsAnd ? "AND" : "NOT"}
                            </Button>
                            <InputBase
                                placeholder="Artist"
                                inputProps={{ 'aria-label': 'search google maps' }}
                                className={classes.searchInputBase}
                                onChange={(event) => {handleArtistTermChange(event.target.value)}}
                            />
                        </Paper>
                    </Grid>
                    <Grid item>
                        <Paper component="form" className={classes.searchPaperSmaller}>
                            <Button variant={"outlined"} aria-label="genre" className={classes.searchIconButton}
                            onClick={() => {dataStore.toggleGenreIsAnd(); setGenreIsAnd(!genreIsAnd)}}>
                                {genreIsAnd ? "AND" : "NOT"}
                            </Button>
                            <Select
                                labelId="tournamentFormatLabel"
                                id="formatSelect"
                                label="Format"
                                className={classes.genreSelect}
                                defaultValue={Constants.C_GENRES[0]}
                                onChange={(event) => {
                                    setGenreTerm(event.target.value);
                                    dataStore.updateGenreTerm(typeof event.target.value === 'string' ? event.target.value:'')
                                }}
                            >
                                {Constants.C_GENRES.map((f, i) => {
                                    return (
                                        <MenuItem value={f} key={i}>{f}</MenuItem>
                                    );
                                })}
                            </Select>
                        </Paper>
                    </Grid>
                    <Grid item>
                        <Button variant={"contained"} onClick={handleSearch}>SEARCH</Button>
                    </Grid>
                </Grid>
            </Grid>

            <Grid item>
                {isLoading &&
                    <CircularProgress />
                }
                {!isLoading &&
                    <Grid container direction={"column"} spacing={4}>
                        <Typography id="modal-modal-description" variant="body1">
                            Result List: {songs.length}
                        </Typography>
                        <TableContainer component={Paper}>
                            <Table className={classes.table} aria-label="simple table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>&nbsp;</TableCell>
                                        <TableCell align="right">Artist</TableCell>
                                        <TableCell align="right">Song</TableCell>
                                        <TableCell align="right">Genre</TableCell>
                                        <TableCell align="right">Language</TableCell>
                                        <TableCell>&nbsp;</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {songs.map((m, i) => {
                                        return (
                                            <TableRow
                                                key={i}
                                                className={classes.tableRow}
                                                onClick={() => {handleOpen(m)}}
                                            >
                                                <TableCell component="th" scope="row">{i}</TableCell>
                                                <TableCell align="right">{m.artist}</TableCell>
                                                <TableCell align="right">{m.song}</TableCell>
                                                <TableCell align="right">{m.genre}</TableCell>
                                                <TableCell align="right">{m.language}</TableCell>
                                                <TableCell align="right">
                                                    <span onClick={() => {handleOpen(m)}}>
                                                        {"View Lyrics"}
                                                    </span>
                                                </TableCell>
                                            </TableRow>
                                        );
                                    })}
                                </TableBody>
                            </Table>
                        </TableContainer>

                        <Modal
                            open={open}
                            onClose={handleClose}
                            aria-labelledby="modal-modal-title"
                            aria-describedby="modal-modal-description"
                        >
                            <Box className={classes.modalBox}>
                                <Typography id="modal-modal-title" variant="h4" component="h2">
                                    {currentSong.artist} - {currentSong.song}
                                </Typography>
                                <Typography id="modal-modal-description" variant="body1" className={classes.modalDescription}>
                                    {currentSong.lyrics}
                                </Typography>
                            </Box>
                        </Modal>
                    </Grid>
                }
            </Grid>
        </Grid>
        )
});


export default Main;



