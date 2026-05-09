export default function Layout(props: LayoutProps<'/[lang]'>) {
    return (
        <div>
            <h1>Layout</h1>
            {props.children}
        </div>
    );
}
