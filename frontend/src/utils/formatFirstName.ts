export const formatFirstName = (name: string) => {
  return name
    ?.split(' ')[0]
    ?.toLowerCase()
    ?.replace(/(?:^|\s)\S/g, (a: string) => a.toUpperCase())
}
