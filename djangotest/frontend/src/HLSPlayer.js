import React, { useEffect, useRef } from 'react';
import videojs from 'video.js';
import 'video.js/dist/video-js.css';
function HLSPlayer({ src }) {
    const videoRef = useRef(null);
    const playerRef = useRef(null);

    useEffect(() => {
        if (!videoRef.current) return;

        // Initialisiere video.js Player
        playerRef.current = videojs(videoRef.current, {
            controls: true,
            autoplay: true,
            preload: 'auto',
            playbackRates: [0.5, 1, 1.5, 2],
        });

        // Ressourcen beim Beenden freigeben
        return () => {
            if (playerRef.current) {
                playerRef.current.dispose();
                playerRef.current = null;
            }
        };
    }, []);

    useEffect(() => {
        if (playerRef.current) {
            playerRef.current.src({ src, type: 'application/vnd.apple.mpegurl' });
        }
    }, [src]);

    return (
        <div>
            <video
                ref={videoRef}
                className="video-js vjs-default-skin"
                width="640"
                height="360"
            ></video>
        </div>
    );
}

export default HLSPlayer;
