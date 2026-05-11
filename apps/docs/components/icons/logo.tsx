import { ComponentProps } from 'react';

export interface TechnoStarLogoProps extends ComponentProps<'svg'> {
    variant?: 'icon' | 'inline';
}
export function TechnoStarLogo({ variant = 'icon', ...others }: TechnoStarLogoProps) {
    const radialGradient1 = `radial-gradient-1`;
    const radialGradient2 = `radial-gradient-2`;
    const radialGradient3 = `radial-gradient-3`;
    const radialGradient4 = `radial-gradient-4`;
    const radialGradient5 = `radial-gradient-5`;
    return (
        <svg viewBox={`${variant === 'icon' ? '0 0 152.01 144.57' : '0 0 523.16 144.57'}`} {...others}>
            <defs>
                <radialGradient id={radialGradient1} cx={76} cy={0} r={85.76} gradientUnits="userSpaceOnUse">
                    <stop offset={0.1} stopColor="#fff" />
                    <stop offset={0.33} stopColor="#dfe6ea" />
                    <stop offset={0.79} stopColor="#00b3cd" />
                </radialGradient>
                <radialGradient
                    id={radialGradient2}
                    cx={-1426.59}
                    cy={-99.88}
                    r={85.75}
                    gradientTransform="translate(542.44 -1275.56) rotate(-72)"
                    gradientUnits="userSpaceOnUse"
                >
                    <stop offset={0.1} stopColor="#fff" />
                    <stop offset={0.33} stopColor="#dfe6ea" />
                    <stop offset={0.79} stopColor="#9689c0" />
                </radialGradient>
                <radialGradient
                    id={radialGradient3}
                    cx={-1795.23}
                    cy={-1559.33}
                    r={85.76}
                    gradientTransform="translate(-502.64 -2184.76) rotate(-144)"
                    gradientUnits="userSpaceOnUse"
                >
                    <stop offset={0.1} stopColor="#fff" />
                    <stop offset={0.33} stopColor="#dfe6ea" />
                    <stop offset={0.79} stopColor="#ee8198" />
                </radialGradient>
                <radialGradient
                    id={radialGradient4}
                    cx={-521.59}
                    cy={-2361.23}
                    r={85.76}
                    gradientTransform="translate(-1691.02 -1471.68) rotate(144)"
                    gradientUnits="userSpaceOnUse"
                >
                    <stop offset={0.1} stopColor="#fff" />
                    <stop offset={0.33} stopColor="#dfe6ea" />
                    <stop offset={0.79} stopColor="#f6ab00" />
                </radialGradient>
                <radialGradient
                    id={radialGradient5}
                    cx={634.98}
                    cy={-1398.27}
                    r={85.76}
                    gradientTransform="translate(-1380.71 -121.45) rotate(72)"
                    gradientUnits="userSpaceOnUse"
                >
                    <stop offset={0.1} stopColor="#fff" />
                    <stop offset={0.33} stopColor="#dfe6ea" />
                    <stop offset={0.79} stopColor="#22ac39" />
                </radialGradient>
            </defs>
            <g id="Layer_2" data-name="Layer 2">
                <g id="\u30ED\u30B4\u30C7\u30FC\u30BF">
                    <polygon
                        fill={`url(#${radialGradient1})`}
                        points="6.62 50.41 59.63 50.41 76 0 54.57 0 44.81 30.02 13.25 30.02 6.62 50.41"
                    />
                    <polygon
                        fill={`url(#${radialGradient2})`}
                        points="33.13 131.97 49.5 81.56 6.62 50.41 0 70.8 25.54 89.35 15.79 119.37 33.13 131.97"
                    />
                    <polygon
                        fill={`url(#${radialGradient3})`}
                        points="118.88 131.97 76 100.82 33.13 131.97 50.47 144.57 76 126.01 101.55 144.57 118.88 131.97"
                    />
                    <polygon
                        fill={`url(#${radialGradient4})`}
                        points="145.38 50.41 102.51 81.56 118.88 131.97 136.22 119.37 126.47 89.35 152.01 70.8 145.38 50.41"
                    />
                    <polygon
                        fill={`url(#${radialGradient5})`}
                        points="76 0 92.38 50.41 145.38 50.41 138.76 30.02 107.19 30.02 97.44 0 76 0"
                    />
                    {variant === 'inline' && (
                        <>
                            <polygon
                                className="fill-[#004ea2] dark:fill-white"
                                points="178.23 51.02 178.23 63.52 181.94 63.52 184.45 55.8 193.47 55.8 193.47 97.39 188.9 98.88 188.9 102.05 204.88 102.05 204.88 98.88 200.31 97.39 200.31 55.8 209.32 55.8 211.83 63.52 215.55 63.52 215.55 51.02 178.23 51.02"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M247.37,85.76H223.85c.3,11.68,7.08,11.55,11,11.55a74.4,74.4,0,0,0,10.48-1.25v4.41a30.8,30.8,0,0,1-10.48,2.26c-8,0-17.2-1.44-17.2-18.89,0-15.33,7.57-18.9,15.29-18.9,7.11,0,15.14,2.82,14.53,18.9ZM232.92,69.07c-5,0-8.69,2.74-9,12.43h17.28C241.21,71.19,237.05,69.07,232.92,69.07Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M383.61,102.73c-7,0-15.89-2.92-15.89-18.89,0-15.63,9-18.9,15.89-18.9s15.89,2.85,15.89,18.9C399.5,100.08,390.57,102.73,383.61,102.73Zm0-33.6c-4.21,0-9.7,2.24-9.7,14.71s6.17,14.63,9.7,14.63,9.71-2.44,9.71-14.63C393.32,71.16,387.83,69.13,383.61,69.13Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M453.37,97.51c-2.34,0-3.44-.48-3.44-3.71V70.37h7.56l.69-4.75h-8.25v-11l-6.51,2.75v8.24h-5.09v4.75h5.09V93.59c0,7.15,3.35,9.14,8.57,9.14a26.88,26.88,0,0,0,7.57-1.23V96.27A27.81,27.81,0,0,1,453.37,97.51Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M317.63,97.49V75.79c0-8.38-4.95-10.85-11-10.85a13.2,13.2,0,0,0-9.91,5V51H286.29v3.17l4.25,1.41V97.47l-4.25,1.41v3.17H301V98.88l-4.24-1.39v-22s3.47-5.62,8.87-5.62c3.3,0,5.84,1.33,5.84,5.15V97.49l-4.25,1.39v3.17h14.68V98.88Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M358.41,97.49V75.79c0-8.38-5-10.85-11-10.85a13.23,13.23,0,0,0-9.92,5v-4.3H327.07V68.8l4.25,1.4V97.49l-4.25,1.39v3.17h14.69V98.88l-4.26-1.39v-22s3.48-5.62,8.88-5.62c3.3,0,5.84,1.33,5.84,5.15V97.5L348,98.88v3.17h14.67V98.88Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M270.9,64.94c-5.77,0-16.66,1.78-16.66,19.1s10.86,18.69,17,18.69a25.71,25.71,0,0,0,8.52-1.92V96.34a63.66,63.66,0,0,1-8.67.9c-4.53,0-10.58-1.88-10.58-13.5,0-12.71,5.71-14.06,10.46-14.06a20.77,20.77,0,0,1,3.69.38L276.59,76v0h3.17V66.74A24.24,24.24,0,0,0,270.9,64.94Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M489.74,97.49V76.76c0-10-5.56-11.82-12.17-11.82a27.39,27.39,0,0,0-11.26,3v8.16h3.17l1.74-5.29a18.44,18.44,0,0,1,5.39-1.19c4.2,0,6.91,1,6.91,6v5h-4.65c-6.49,0-14.65,1.39-14.65,11.36,0,9.82,5.95,10.75,10.64,10.75a13.79,13.79,0,0,0,8.66-3.16v2.48H494V98.88Zm-13.44.23c-3.24,0-5.58-.18-5.58-6.29s3.82-6.89,9.74-7l3.06,0V95.08C481.83,96.21,479.06,97.72,476.3,97.72Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M517.69,64.94a9.89,9.89,0,0,0-8.13,4.58V65.63H499.13V68.8l4.25,1.4V97.47l-4.25,1.41v3.17h14.68V98.88l-4.25-1.38V76.9c0-2.76,3.49-6.69,7.38-6.43a10.39,10.39,0,0,1,1.23.17L520,76.22h3.17V65.35A44.07,44.07,0,0,0,517.69,64.94Z"
                            />
                            <path
                                className="fill-[#004ea2] dark:fill-white"
                                d="M422.65,75.44l-4-2.52c-3-2.13-5.66-3.85-5.66-7.42,0-5,3.49-7.5,8.22-7.5a20.93,20.93,0,0,1,4.78.75l2.59,8h3.16v-11s-5.65-2.46-10.53-2.46c-6.32,0-14.27,3.11-14.27,12.8,0,5.63,3.6,8.93,7.51,11.62l5.12,3.2c3.16,2.13,7.19,4.31,7.19,8.57,0,6.26-4.82,8.41-9.43,8.41a20.18,20.18,0,0,1-4.61-.75l-2.45-7.55h-3.18v10.87s5.78,2.31,10.38,2.31c7.49,0,15.48-2.22,15.48-13.77C432.94,82,427,78.46,422.65,75.44Z"
                            />
                        </>
                    )}
                </g>
            </g>
        </svg>
    );
}
