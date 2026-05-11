type VideoProps = React.VideoHTMLAttributes<HTMLVideoElement>;

export function Video(props: VideoProps) {
    return (
        <video
            controls
            playsInline
            muted={true}
            style={{
                width: '100%',
                height: '100%',
                borderRadius: 12,
            }}
            {...props}
        />
    );
}
